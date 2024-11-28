---
title: "Jekyll 테마 404 에러 해결"
tags:
    - 404
    - error
date: "2024-11-28"
thumbnail: "/assets/img/Project/GitBlog/post-06/thumbnail.png"
---

며칠 깃 블로그 관리 안하다가, 다시 여유되서 마크다운 파일 몇개 푸시했는데, 분명 존재하는 파일인데 404가 발생했다.
작성했던 페이지를 제대로 로드는 하지만, 해당 페이지 경로를 들어가도 작성했던 페이지가 뜨는게 아니라, 404가 뜨는 것이다.

특이하게 기존에 작성해뒀던 페이지들은 이상없이 잘 동작해서, 특정 경로에 띄어쓰기(공백)이 있어서인가 싶었으나 그것도 아니였다.

결국 로컬에서 jekyll을 설치하고, 한번 실행해가며 해결해나간 과정을 작성해본다.

## Readme.md Installation을 따르며, 단계를 빼먹지 말자.

처음 해당 블로그를 설치할 적, 단순히 fork한 후 내 입맛에 맞춰 `_confing.yml`파일 수정해서 page를 추가해나가는 식으로만 진행했다.
완전히 새로운 내용들 작성하는 것보다 기존 내용을 조금씩 수정하며 익숙해지는게 편해서였는데, 이로인해 빼먹은 내용들이 일부 있었다.

- 참고 : [Jekyll 테마 적용](https://kangspa.github.io/Project/GitBlog/post-01.html)

참고 링크의 과정들을 따르고나면, 이제 아래와 같은 과정을 따르면 좋을 것이다.
***아래 작성하는 모든 과정은, `Readme.md`의 `Installation` 중 `Method 2`를 Window 환경에 맞춰서 풀어서 작성한 것이다.***
![Image1](/assets/img/Project/GitBlog/post-06/1.png)

1. <https://rubyinstaller.org/downloads/>에서 'RubyInstallers with Devkit'을 다운받고, 설치한다.
    ![Image2](/assets/img/Project/GitBlog/post-06/2.png)

2. 다 설치되고나서 cmd창에서 열겠다고 그대로 진행하면, cmd 창에서 뭔가 많은 내용들이 뜨고 선택해서 설치하라는 내용이 나올 것이다.
    그 중 `MSYS2 and MINGW development toolchain`에 해당하는 3번(기억상입니다)을 선택하기 위해, 3을 입력하고 엔터를 눌러준다.

3. 이후 새로운 cmd 창을 열어서 `gem install jekyll bundler` 를 입력해주면, jekyll 설치가 진행된다.
    필자는 여기서 한 번 막혔는데, PC 재부팅한 후 진행하니까 되서 혹시나 여기서 막힌다면 재부팅 해보는 것도 추천한다.
    설치가 다 됐다면 `jekyll -v`를 입력해서 jekyll 버전이 뜨는지 확인할 수 있다.

4. 현재 프로젝트(`{username}.github.io`)의 Gemfile 최하단에 `gem "jekyll-theme-satellite"`를 작성해준다.
    ![Image3](/assets/img/Project/GitBlog/post-06/3.png)

5. 현재 프로젝트(`{username}.github.io`) 위치에서 cmd를 열어준다.
    VScode로 진행 중이라면 그냥 해당 폴더(프로젝트)에서 터미널 열어주면 된다.

6. 열어둔 cmd 창에 `bundle install` 을 입력해서 현재 프로젝트의 내용들을 설치해준다.
    필자는 이 단계에서 `an error occurred while installing wdm (0.1.1), and bundler cannot continue.` 이런 에러가 뜨면서 진행이 불가했다.
    [Newbie problems with wdm errors](https://talk.jekyllrb.com/t/newbie-problems-with-wdm-errors/9233)를 참고하여, 그냥 지우라는 말이 있길래 주석처리를 하고 진행해보았다.
    ![Image4](/assets/img/Project/GitBlog/post-06/4.png)
    ![Image5](/assets/img/Project/GitBlog/post-06/5.png)
    이후 설치에 에러 없이 진행되는 것을 볼 수 있었다.

7. 마지막으로 `bundle exec jekyll serve` 를 입력하여 로컬에서 jekyll 테마를 열 수 있다. 주소는 <localhost:4000>로 열린다.
    일부 Warning 코드들이 발생하는데, 읽어보면 Sass 3.0.0. 에서 지워질 css 문법이라 주의하라는 내용으로 보인다.
    ![Image6](/assets/img/Project/GitBlog/post-06/6.png)
    추후 문제가 될 경우 수정해도 되지 않을까 생각되어 당장 건들지는 않았다. 무엇보다 Gemfile에 이것저것 버전 명시가 되어있으니 큰 문제는 없지 않을까 생각하기도 했다.

사실 [특정 블로그 글](https://iamheesoo.github.io/blog/gitblog-sol-jekyll)을 보면 이렇게 jekyll 테마를 한번 실행해주면 문제가 발생하지 않는 듯하다.(보안상 이유)

---

필자의 경우, 추가로 `/assets/img/thumbnail/empty.jpg` 가 없다고 thumbnail 없는 포스트를 열 때 썸네일 로드를 못하는 오류가 있었다.
이는 내가 해당 폴더의 이미지들 쓸 일이 없겠지 생각해서 삭제했던 부분이었는데, 해당 오류가 발생하는 것을 확인한 후 원복시켰다.

아마 기존에 작성한 포스트도 썸네일을 비워뒀었는데, 그 때는 404 에러가 안 떳던걸 보면 해당 부분은 404 에러에 직접적인 영향은 없었으리라 생각된다.
다만 이것까지 하고나서 404 에러가 안 뜨는 것을 확인한만큼, 혹시나 하는 마음에 함께 작성해둔다.