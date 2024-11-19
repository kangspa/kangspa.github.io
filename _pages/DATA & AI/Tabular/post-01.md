---
title: "파이썬 중복 데이터 처리 방법"
tags:
    - Python
    - 데이터 처리
date: "2024-11-19"
---

## 데이터프레임에서 중복 제거

```
df.drop_duplicates()
```

default 그대로 사용하면, 모든 열 기준으로 중복을 제거한다.
파라미터로 ['col']을 지정해주면 해당 열 기준으로 제거해준다.
- keep : 남길 대상 지정 / first, last, False 가 있다. (False 는 모두 제거)
- ignore_index : boolean 값으로 입력해서, True 입력 시 인덱스가 재설정된다.

- 출처 : <https://mizykk.tistory.com/93>

## 리스트에서 중복 제거

1. set 활용
    set 자료구조는 데이터에 중복된 값이 없다는 특징을 활용한다.
    ex) `list(set('중복제거하려는 리스트'))`

2. for 반복문
    중복 제거된 값이 저장될 별도의 리스트를 만들고, 해당 리스트에 이미 있는 값은 제외하면서 원본 리스트를 반복문 돌리며 값을 넣는다.
    ```python
    arr = [] # 원본 리스트
    result = [] # 결과 리스트

    for v in arr:
        if v not in result:
            result.append(v)
    ```

3. dict 활용
    딕셔너리의 키 값이 중복 불가인 성질을 활용해준다.
    ex) `list(dict.fromkeys('중복제거하려는 리스트'))`

- 출처 : <https://blockdmask.tistory.com/543>