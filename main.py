import sys
import asyncio
from pyppeteer import launch
from textblob import TextBlob
from googletrans import Translator

VIDEO_NAO_DISPONIVEL = 'Este vídeo não está mais disponível'

async def get_comments(video_url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(video_url)
    
    print('Indo ate a pagina, será aguardado 10 sec')
    
    await page.waitFor(5000)
    await page.evaluate("""{window.scrollBy(0, 100000000);}""")  # scroll to end of site 
    await page.waitFor(5000)
    
    print('Verificando se é um vídeo disponivel')
    
    isIdVideoNaoValido = await page.querySelector('#contents > ytd-background-promo-renderer > div.promo-message.style-scope.ytd-background-promo-renderer > div') # verifica se o vídeo esta disponivel

    if isIdVideoNaoValido is not None:
        textIsIdVideoNaoValido = await page.evaluate('(element) => element.textContent', isIdVideoNaoValido)
        if VIDEO_NAO_DISPONIVEL == textIsIdVideoNaoValido:
            logging_error_get_video()
            await browser.close()
            return []

    print('Aguardando o carregamento dos comentários')

    await page.waitForSelector('#contents')  # aguarda o carregamento da seção de comentários
    comments = []
    while True:
        comment_elements = await page.querySelectorAll('#contents ytd-comment-thread-renderer')
        for element in comment_elements:
            comment = await element.querySelector('#content-text')
            comment_text = await page.evaluate('(element) => element.textContent', comment)
            comments.append(comment_text)
        break
    await browser.close()
    
    print('Retornando os comentarios')
    
    return comments

def logging_error_get_video():
    print('----------------------------------------------------------------')
    print('Informe um id de vídeo valido, exemplo de um valido: jNQXAC9IVRw')
    print('Exemplo de como informar um id valido abaixo:')
    print('python main.py jNQXAC9IVRw')
    print('----------------------------------------------------------------')


def get_sentimentos_comentario(comentario):
    translator = Translator()
    language = translator.detect(comentario).lang

    if language != 'en':
        traducao = TextBlob(str(translator.translate(comentario, dest='en').text))
        print('----------------------------------------------------------------')
        print('Comentario: {0} - Sentimento: {1}'.format(traducao, traducao.sentiment.polarity))
        print('----------------------------------------------------------------')
    else:
        text = TextBlob(comentario)
        print('----------------------------------------------------------------')
        print('Comentario: {0} - Sentimento: {1}'.format(text, text.sentiment.polarity))
        print('----------------------------------------------------------------')

if __name__ == '__main__':

    VIDEO_ID = None

    if len(sys.argv) >= 2 and sys.argv[1] is not None:
        VIDEO_ID = sys.argv[1]
        video_url = 'https://www.youtube.com/watch?v={0}'.format(VIDEO_ID)
        comments = asyncio.get_event_loop().run_until_complete(get_comments(video_url))
        
    
        print('Passando os comentarios para analise de sentimento')
        
        if len(comments) > 0:
            for comment in comments:
                get_sentimentos_comentario(comment)
        else:
            print('Não foi possivel obter os comentários')
    else:
        logging_error_get_video()