# Bubble Sort

氣泡排序法的 Python 實作

## 說明

氣泡排序（Bubble Sort）是一種簡單的排序演算法，透過重複比較相鄰元素並交換位置來達成排序。

## 時間複雜度

- 平均：O(n²)
- 最佳：O(n)（已排序時）
- 最差：O(n²)

## 空間複雜度

O(1)

## 使用方法

```python
from bubble_sort import bubble_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

## 執行

```bash
python bubble_sort.py
```