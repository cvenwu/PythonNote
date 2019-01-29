

# 创建一个普通列表
member = ['小甲鱼', '小布丁', '黑夜']
print(member)
print(type(member))
print(len(member))

# 创建一个混合列表
mix = [1, '小甲鱼', 3.14, [1, 2, 3]]

# 向列表添加元素
member.append('自己')
print(member)
print(len(member))

# 使用一个列表扩展另一个列表
member2 = ['year', 'month']
member.extend(member2)
print(member)
print(member2)


# 向指定位置插入元素
member.insert(1, '吴晓文') # 实际插入到第2个位置
print(member)
