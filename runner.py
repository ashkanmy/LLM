from src.loader.PrepareLoader import create_dataloader_v1
from loguru import logger

pathString = '/Users/mansoash/LLM/src/db/story.txt'
logger.add('/Users/mansoash/LLM/src/logs/logs.log')

#define decoration
@logger.catch
def readData(pathString):    
    with open(pathString, "r", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text



# catch the error
try:
    raw_text = readData(pathString)
except:
    logger.error("no file exists!")
 # load dataset   
dataloader = create_dataloader_v1(raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
data_iter = iter(dataloader)
first_batch = next(data_iter)
print(first_batch)
