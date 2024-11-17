---
title: "로딩 화면 수정(시간 줄이기)"
tags:
    - loading
    - satellite
    - 시간 단축
date: "2024-11-17"
thumbnail: "/assets/img/Project/GitBlog/post-05/thumbnail.png"
---

해당 테마는 다 좋았지만, 각 카테고리 넘어갈 때마다 로딩 화면이 나오고, 심지어 로딩 애니메이션이 갖는 시간이 길다는 점이 불편했다.
확인해보니 `assets/js/subject.js` 파일에서 로딩 애니메이션 시간이 0.75초로 설정된 것을 볼 수 있었다.
```javascript
// Loading page
window.addEventListener("load", () => {
    var load_div = document.querySelector('#loading');

    if(load_div != null){
        setTimeout(function(){
            load_div.style.transition = '.75s';
            load_div.style.opacity = '0';
            load_div.style.visibility = 'hidden';
        }, 800);
    }
});
```

여기서 `load_div.style.transition` 값을 `.25s` 로 바꿔주면 로딩 애니메이션을 0.25초로 바꿔줄 수 있다.
인터넷만 빠르다면 이전보다 최소 0.5초는 로딩 시간을 줄일 수 있다.

- 수정 결과
    ```javascript
    // Loading page
    window.addEventListener("load", () => {
        var load_div = document.querySelector('#loading');

        if(load_div != null){
            setTimeout(function(){
                load_div.style.transition = '.25s';
                load_div.style.opacity = '0';
                load_div.style.visibility = 'hidden';
            }, 800);
        }
    });
    ```

---

추가로 로딩 애니메이션 자체를 없애려면, `_layouts/page.html` 파일의 `.inner-content` 요소에서 `{% include loading.html %}` 부분을 주석처리해주면 된다.
다만 모든 로딩 애니메이션이 사라져서 좀 밋밋하기에, 필자는 주석처리를 하진 않고 그냥 시간만 0.1초로 줄여봤다.

```html
<div class="inner-content">
    {% include category.html %}
    {% if page_type == "category" %}
        <!-- {% include loading.html %} -->
        {% include pagination.html %}
    {% else %}
        {% include post.html %}
    {% endif %}
</div>
```