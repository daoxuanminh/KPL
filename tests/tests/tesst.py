def tim_so_nho_thu_hai(mang):
    min1 = float("inf")
    min2 = float("inf")

    for so in mang:
        if so < min1:
            min2 = min1
            min1 = so
        else:
            min2 = so

    return min2


# Ví dụ
mang = [3, 5, 5]
so_nho_thu_hai = tim_so_nho_thu_hai(mang)
print("Số nhỏ thứ hai trong mảng là:", so_nho_thu_hai)
