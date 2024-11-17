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