import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import date
from pathlib import Path

url = ""
if not url.startswith("https"): url = "https://" + url

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

with open("test.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify()) 

today = date.today().strftime("%Y-%m-%d")
if urlparse(url).netloc == "www.acmicpc.net":
    directory = "Baekjoon"
    title = soup.select_one("#problem_title").text.strip()
    title = title.replace("/", "⧸").replace("|", "｜").replace(":", "：").replace("?", "？").replace("*", "＊").replace('"', "＂").replace("<", "＜").replace(">", "＞")  # 특수문자 제거
    tags = [tag.text.strip() for tag in soup.select("#problem-info td") if tag.text.strip().endswith("초") or tag.text.strip().endswith("MB") or tag.text.strip().endswith("%")]
    description = soup.select_one("#problem-body").decode_contents()
elif urlparse(url).netloc == "school.programmers.co.kr":
    directory = "Programmers"
    title = soup.select_one(".challenge-title").text.strip()
    title = title.replace("/", "⧸").replace("|", "｜").replace(":", "：").replace("?", "？").replace("*", "＊").replace('"', "＂").replace("<", "＜").replace(">", "＞")  # 특수문자 제거
    tags = [tag.text.strip() for tag in soup.select(".dropdown-language .dropdown-item")]
    description = soup.select_one(".guide-section-description").decode_contents()

with open(f"_pages/{directory}/{title}.md", "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write(f"title: \"{title}\"\n")
    f.write("tags:\n")
    for tag in tags:
        f.write(f"    - {tag}\n")
    f.write(f"date: \"{today}\"\n")
    f.write("---\n\n")
    f.write(f"출처 : [{title}]({url})\n")
    f.write("<details>\n")
    f.write("<summary><b>Solution</b></summary>\n\n")
    folder = Path(f"_pages/{directory}/code")
    files = [f for f in folder.iterdir() if f.is_file() and f.name.startswith(title)]
    for file in files:
        with open(file, "r", encoding="utf-8") as code_file:
            code_content = code_file.read()
            if str(file).endswith(".py"):
                f.write("<details>\n")
                f.write("<summary>Python</summary>\n\n")
                f.write(f"<pre><code class='language-python'>\n{code_content}\n</code></pre>\n")
                f.write("</details>\n\n")
            elif str(file).endswith(".c"):
                f.write("<details>\n")
                f.write("<summary>C</summary>\n\n")
                f.write(f"<pre><code class='language-c'>\n{code_content}\n</code></pre>\n")
                f.write("</details>\n\n")
            elif str(file).endswith(".cpp"):
                f.write("<details>\n")
                f.write("<summary>C++</summary>\n\n")
                f.write(f"<pre><code class='language-cpp'>\n{code_content}\n</code></pre>\n")
                f.write("</details>\n\n")
            elif str(file).endswith(".java"):
                f.write("<details>\n")
                f.write("<summary>Java</summary>\n\n")
                f.write(f"<pre><code class='language-java'>\n{code_content}\n</code></pre>\n")
                f.write("</details>\n\n")
            elif str(file).endswith(".js"):
                f.write("<details>\n")
                f.write("<summary>JavaScript</summary>\n\n")
                f.write(f"<pre><code class='language-javascript'>\n{code_content}\n</code></pre>\n")
                f.write("</details>\n\n")
    f.write("</details>\n\n")
    f.write("<hr>\n")
    f.write(description)
        