["Attention Is All You Need"](https://arxiv.org/html/1706.03762v7) 논문 내용 리뷰 및 정리한다.

# 3 Model Architecture
![Figure 1](https://arxiv.org/html/1706.03762v7/extracted/1706.03762v7/Figures/ModalNet-21.png)

```markdown
많은 경쟁력 있는 신경망 시퀀스 변환 모델은 "encoder-decoder" 구조를 갖습니다. 여기 인코더는 기호 표현의 입력 시퀀스 (x_1, ..., x_n)를 연속적인 표현의 시퀀스 z=(z_1, ..., z_n)으로 맵핑합니다.
z가 주어졌을 때, 디코더는 기호의 출력 시퀀스 (y_1, ..., y_n)을 하나씩 생성합니다. 각 단계에서 모델은 "auto-regressive" 모델이고, 이전에 생성된 기호들을 다음 생성을 위한 추가 입력으로 소모합니다.

Transformer는 "self-attention", "point-wise", "fully connected layers"를 인코더와 디코더 모두에 쌓는데 사용하여 이러한 전체 구조를 따릅니다. 이는 Figure1의 좌우 절반씩에서 표현되어 있습니다.
```

Transformer 구조도 일반적인 `encoder-decoder` 구조를 따르며, 인코더 디코더 양쪽에 "self-attention", "point-wise", "fully connected layers"를 쌓아올림으로써 구축했다고 한다.

- `Auto-regressive model (자기 회귀 모형)`
    시간에 따라 변하는 특정 프로세스를 설명하는데 사용되며, 출력 변수가 자신의 이전 값과 확률적 항에 선형적으로 의존함을 지정한다.
    - 출처
        - <https://ko.wikipedia.org/wiki/자기회귀모형>

## 3.1 Encoder and Decoder Stacks

### Encoder
```markdown
인코더는 6개의 동일한 레이어가 쌓여서 구성되었습니다. 각 레이어는 2개의 서브 레이어를 갖고 있습니다.
첫번째는 "multi-head self-attention" 매커니즘이고, 두번째는 간단한, "position-wise fully connected feed-forward network" 입니다.
우리는 잔차 연결을 각 2개의 서브 레이어에 적용하고, 레이어 정규화를 진행합니다. 각 서브 레이어의 출력은 `LayerNorm(x + Sublayer(x))`로, `Sublayer(x)`는 해당 서브 레이어입니다.
잔차 연결을 구현하기 위해서는, 모델의 임베딩 레이어 뿐만 아니라, 모든 서브 레이어는 출력 차원이 `d_model = 512`로 구현됩니다.
```

### Decoder
```markdown
디코더도 6개의 동일한 레이어가 쌓여서 구성됩니다. 각 인코더 레이어는 2개의 서브 레이어로 구성됐는데, 디코더는 인코더 스택의 출력에 "multi-head attention"을 수행하는 3번째 서브 레이어가 추가됩니다.
인코더와 유사하게, 우리는 각 서브 레이어에 대해 잔차 연결을 적용하고 레이어 정규화를 진행합니다.
또한 이후 서브 시퀀스 위치에 주목하는 것을 방지하기 위해 디코더 스택 안의 "self-attention sub-layer"를 변형합니다.
출력 임베딩은 한 자리씩 오프셋 되는 것에 결합된 마스킹 기법은 i 위치가 오직 i보다 작은 위치의 출력만 의존하게된다는 예측을 보장합니다.
```

인코더와 디코더는 유사한 구조를 갖는데, 디코더는 "multi-head attention" 레이어가 하나 추가되는게 차이점이다.
또한 헤당 레이어는 인코더의 출력에 대한 값을 수행하는데, 이를 통해 인코더 값을 활용해서 디코더가 사용자가 원하는 출력을 도출해주는 것으로 보인다.

Figure1 이미지를 보면 왼쪽의 인코더를 통해 도출된 출력이, 디코더에서 2번째 단계의 "Multi-Head Attention"에 입력되는 것을 볼 수 있다.
해당 "Multi-Head Attention" 레이어의 출력과 디코더 내의 이전 서브 레이어에서 출력된 값을 함께 정규화 진행 후, "position-wise fully connected feed-forward network" 로 입력되는 것을 볼 수 있다.

## 3.2 Attention

```markdown
어텐션 함수는 query와 key-value 쌍을 출력으로 맵핑하는 함수로 설명됩니다. 이 때 query, keys, values는 모든 벡터의 출력입니다.
이 출력은 값들의 가중치 합으로 계산되며, 각 값에 할당된 가중치는 query와 연관되는 key의 호환성 함수에 의해 계산됩니다.
```

![Figure 2](https://arxiv.org/html/1706.03762v7/extracted/1706.03762v7/Figures/ModalNet-20.png)

### 3.2.1 Scaled Dot-Product Attention

```markdown
우리는 우리들의 어텐션 구조(Figure 2)를 "Scaled Dot-Product Attention"라고 부릅니다.
입력은 query, d_k 차원의 key, d_v 차원의 value로 구성됩니다.
우리는 모든 key와 query의 내적을 계산하고, 각각을 sqrt(d_k)로 나눈 뒤, softmax 함수를 적용해서 value의 가중치를 얻습니다.

실제로 우리는 행렬 Q로 query 묶음들을 묶어서 동시에 어텐션 함수에 계산합니다. key와 value들은 각각 K, V 행렬로 묶입니다. 우리는 아래와 같은 수식으로 계산합니다.
```
$$
\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^\top}{\sqrt{d_k}} \right)V
$$
```markdown
두가지 보편적인 어텐션 함수는 "Additive attention"과 "Dot-product attention"입니다.
"Dot-product attention"은 1/sqrt(d_k)로 스케일링 한다는 것을 제외하면, 우리 알고리즘과 동일합니다. "Additive attention"은 단일 은닉층이 적용된 "feed-forward" 구조를 사용한 호환성 함수로 계산됩니다.
이론상 복잡도는 유사하지만, "Dot-product attention"은 높은 최적화된 행렬곱 코드 활용이 가능하여, 훨씬 빠르고 공간 효율성이 뛰어납니다.

d_k 값이 작을 때, 두 어텐션 방식은 유사한 성능을 보이지만, d_k값이 클 경우 스케일링 없는 "Dot-product attention"보다 "Additive attention"이 더 좋은 성능을 보입니다.
우리는 d_k 값이 클수록 내적 값들이 커진며, 이로 인해 softmax 함수가 매우 작은 기울기를 갖게된다고 보았습니다. 이를 상쇄하기 위해, 우리는 1/sqrt(d_k)로 스케일링합니다.
```

`Dot-Product Attention` 함수를 사용하면서, 기존에 사용되던 함수에 살짝 변형($1/\sqrt(d_k)$)을 준 것을 볼 수 있다.
이는 기울기 소실 문제 해결을 위한 것으로 보인다.

### 3.2.2 Multi-Head Attention

```markdown
d_model 차원의 key, value, query를 단일 어텐션 함수로 진행하는 대신, 우리는 query, key, value를 각각의 d_k, d_k, d_v 차원으로 h 횟수만큼 선형 투영하는 것이 좋다는 것을 발견했습니다.
각각의 투영된 query, key, value에 대해 병렬로 어텐션 함수를 수행하면, d_v 차원 출력 값이 생성됩니다. 이걸 합치고 다시 한번 투영시켜, Figure 2와 같은 결과를 만들어냅니다.

"Multi-head attention"은 다른 위치에서 다른 표현 공간의 정보를 동시에 참조할 수 있도록 해줍니다. 단일 어텐션 헤드와 함께 사용 시, 이게 평균화됩니다.
```
$$
\begin{aligned}
\text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O \\
\text{where} \quad \text{head}_i &= \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)
\end{aligned}
$$

$$
W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}, \quad
W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}, \quad
W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}, \quad
W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}
$$
```markdown
투영에 사용된 파라미터 행렬은 위와 같습니다.

이 연구에서 우리는 h = 8 인 병렬 어텐션 레이어 혹은 헤드를 사용합니다.
각각의 레이어(헤드)에서 우리는 d_k = d_v = d_model / h = 64 로 설정했습니다.
각 헤드의 차원이 작아졌기 때문에, 총 연산 비용은 전체 차원에서 단일 헤드 어텐션을 수행하는 것과 유사합니다.
```

query, key, value 각각에 대해 변환 및 연산 진행을 한 후, 합치고 다시 선형 변환 시키는 것이 단일 어텐션 연산보다 유리하다.
연구팀은 각각의 레이어에서 차원 값을 작게 설정함으로써, 단일 어텐션 연산과 연산 비용에서 큰 차이가 발생하지 않도록 하였다.

### 3.2.3 Applications of Attention in our Model