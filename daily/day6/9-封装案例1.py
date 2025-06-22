# 作者: 王道 龙哥
# 2025年06月02日14时44分09秒
# xxx@qq.com
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 在类内部声明并初始化其他的属性
        self.free_area = area
        self.item_list = []

    def __str__(self) -> str:
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s 总面积：%.2f[剩余：%.2f] 家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


    def add_item(self, item: HouseItem) -> None:
        # 传入 item 参数 ， 参数形式为 HouseItem  虽然 :HouseItem 是注解，但方便后面补全代码
        """
        HouseItem是注解，方便高效写代码的
        :param item:
        :return:
        """
        print("要添加 %s" % item)
        # 1. 判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中" % item.name)

            return

        # 2. 将家具的名称追加到名称列表中
        self.item_list.append(item.name)

        # 3. 计算剩余面积
        self.free_area -= item.area


if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    print(chest)
    house = House('两室一厅', 60)
    house.add_item(bed)
    print(house)
