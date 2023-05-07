# Poc Analise Sentimento Comentarios Youtube

Poc simples para testar as libs pyppeteer, textblob e googletrans...

Não usei a api oficial do youtube porque queria que fosse algo simples, sem precisar ficar pegando Keys e afins e tanbém não queria fazer para todos os comentarios sendo assim só o primeiro carregamento já me satisfaz...

## Requerimentos

```bash
pip3 install -r requirements.txt
python -m textblob.download_corpora
```

## Links uteis
https://pyppeteer.github.io/pyppeteer/
https://py-googletrans.readthedocs.io/en/latest/


## Exemplo de execução

```
$ python3 main.py jNQXAC9IVRw
```

## Resultado

```
Indo ate a pagina, será aguardado 10 sec
Verificando se é um vídeo disponivel
Aguardando o carregamento dos comentários
Retornando os comentarios
Passando os comentarios para analise de sentimento
----------------------------------------------------------------
Comentario: We're so honored that the first ever YouTube video was filmed here! - Sentimento: 0.3125
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: And then a platform, an entire culture, was born. - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Going back here to review this artwork every like I'll be back to watch again! - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: This is the definition of nostalgia - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Historical moments .. years later, Me at the zoo has become a noun. - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: This Will Forever Be An Important Thing In Human History. - Sentimento: 0.2
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: That video that will never get old - Sentimento: 0.1
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: an oldie but a goodie - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Incredible. - Sentimento: 0.9
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: The first shocking YouTube video! - Sentimento: -0.375
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Jawed FINNALY came back! - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: I visit this video every couple months for the nostalgia - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: plot twist: this is actually a full lenght video but it was cut in the middle of transitioning - Sentimento: 0.175
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Funny 
Educational 
Straight to the point 
No sponsors 
Awesome haircut 
Elephants 
There is nothing this man can’t do! - Sentimento: 0.425
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: And it was facing a simple 19 -second test video that one of the largest video platforms was born - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: they need to make this a series with facts of all animals - Sentimento: 0.0
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: This video is already 18 yrs old. Where tf did time go? - Sentimento: 0.1
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: Wow,I was two months old when this masterpiece came out. - Sentimento: 0.1
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: This video was 15 or was 16 years old when I first saw it, now it already has 18 - Sentimento: 0.175
----------------------------------------------------------------
----------------------------------------------------------------
Comentario: 2 million subscribers with one video. LEGEND - Sentimento: 0.0
----------------------------------------------------------------

```