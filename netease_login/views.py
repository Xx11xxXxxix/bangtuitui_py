import asyncio
import re
import time
from django.shortcuts import render
import requests
import base64
from io import BytesIO
from PIL import Image
from django.http import JsonResponse, HttpResponse
from asgiref.sync import sync_to_async
from netease_login.models import EaseapiUser, EaseapiLog

BASE_URL = "http://127.0.0.1:3000"


async def netEase_login(request):
    try:
        unikey, qr_image = await get_qr_code()
        status_task = asyncio.create_task(check_scan_status_async(unikey))
        # response = HttpResponse(qr_image.getvalue(), content_type='image/png')
        # response['Content-Disposition'] = 'inline;filename="qr.png"'
        # response['X-Unikey'] = unikey
        #
        # response = JsonResponse({
        #     'unikey': unikey,
        #     'qr_image': base64.b64encode(qr_image.getvalue()).decode()
        # })
        html_content = f"""
          <html>
          <body>
              <p>UniKey: <span id="unikey">{unikey}</span></p>
              <img src="data:image/png;base64,{base64.b64encode(qr_image.getvalue()).decode()}" alt="QR Code">
          </body>
          </html>
          """
        return HttpResponse(html_content, content_type='text/html')
        # return response
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@sync_to_async
def get_qr_code():
    url = f"{BASE_URL}/login/qr/key"
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({"error": "meiunikey"}, status=400)
    unikey = response.json()["data"]["unikey"]

    # 二维码
    url = f"{BASE_URL}/login/qr/create?key={unikey}&qrimg=true"
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({"error": "qrshibai"}, status=400)
    qrimg = response.json()["data"]["qrimg"]

    qr_bytes = base64.b64decode(qrimg.split(",")[1])
    qr_image = BytesIO(qr_bytes)
    return unikey, qr_image


async def check_scan_status_async(unikey):
    try:
        for _ in range(10):
            status = await sync_to_async(check_scan_status)(unikey)
            print(f"Checking status: {status}")
            if status["code"] in [800, 803]:
                print(f"Status changed: {status['code']}")
                return JsonResponse({
                    "status": "success" if status["code"] == 803 else "expired",
                    "cookies": status.get("cookies")
                })
            await asyncio.sleep(2)
    except Exception as e:
        print(f"check_scan_status_async cuole: {e}")
        return JsonResponse({"error": str(e)}, status=500)


#todo 等wenjie写前端轮询二维码扫描状态以及浏览器储存cookie
def check_scan_status(unikey):
    url = f"{BASE_URL}/login/qr/check?key={unikey}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"code": -1}



async def check_status(request):
    try:
        unikey = request.GET.get('key')
        if not unikey:
            return JsonResponse({"error": "No key"}, status=400)

        status = await sync_to_async(check_scan_status)(unikey)

        await EaseapiLog.async_api_log(
            api_name='check_status',
            request_params={'key': unikey},
            response_data=status,
            status_code=status.get('code')
        )

        if status.get('code') == 803:
            cookies = status.get('cookie')
            music_u = extract_music_u(cookies)

            user_info = await get_user_info(music_u)

            if user_info.get('code') == 200:
                profile = user_info['profile']
                await sync_to_async(EaseapiUser.update_user)(profile, music_u)
        return JsonResponse(status)
    except Exception as e:
        await EaseapiLog.async_api_log(
            api_name='check_status',
            request_params={'key': request.GET.get('key', 'N/A')},
            response_data=None,
            status_code=-1,
            error_message=str(e)
        )
        return JsonResponse({"error": str(e)}, status=500)

def extract_music_u(cookies):
    ##Cookie
   pattern = r'MUSIC_U=([^;]+)'
   match = re.search(pattern, cookies)
   return match.group(1) if match else None


async def get_user_info(music_u):
    #todo 测试用cookie别几把老调容易封号
    # url = f"{BASE_URL}/user/account?cookie=MUSIC_U=009B0CEDEE0769E534E6C0FD6488ECF21E6B0B450EB9AF4AB77853E7A1D5A25051BA4FCB535A2F4B1D9CFE43ADB0B76BD80070EF33916DC4EAF07F32654CEFE6695864A1BFA5F304EA60E790B96068226220292B8C24150E54383C4EEEE2DA0D27A842227D5068B047BE0923FE3B91D90C24BAA31A721CDB74C427D9C2161FF576F37D2C2BA3E6417F11E4723F02533937C4C0B6A7BD43D8F4A3F37A7AB176D5FF5CCE2CEFC9F7B529337767EDFF18E0A8853A82853262E7A9E954E3E70ED6A829E2BF8219F9FF50E8BE1CF5468BD7479201752252F5BDC38E13A433C7B270DF9DEA6FB3C9CC257940B488C63F4FEC47B57A01B0428D1D6780245CFB65F278653ABB857367A5BCE5A5580972346370B1EF7B43ED9D8A325DE5982E5002095D6E"

    # url = f"{BASE_URL}/user/account?cookie=MUSIC_U={music_u}"
    # headers = {'Cookie': f'MUSIC_U={music_u}'}
    try:
        response = await sync_to_async(requests.get)(url)
        data = await sync_to_async(lambda: response.json())()

        await EaseapiLog.async_api_log(
            api_name='get_user_info',
            request_params={'music_u': music_u},
            response_data=data or {},
            status_code=data.get('code', -1) if data else -1
        )

        if data and data.get('code') == 200:
            profile = data.get('profile')
            if profile:
                await sync_to_async(EaseapiUser.update_user)(profile, music_u)
        return JsonResponse(data or {})
    except Exception as e:
        print("又几把报错操:", str(e))
        await EaseapiLog.async_api_log(
            api_name='get_user_info',
            request_params={'music_u': music_u},
            response_data={},
            status_code=-1,
            error_message=str(e)
        )
        return JsonResponse({'code': -1, 'msg': str(e)})