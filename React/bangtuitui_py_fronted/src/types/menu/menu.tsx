export interface MenuItem {
    access_id: number;
    name: string;
    path: string;
    parent_id: number;
    sort: number;
    icon: string;
    redirect_name: string | null;
    is_route: boolean;
    is_menu: boolean;
    alias: string;
    is_show: boolean;
    children?: MenuItem[];
  }