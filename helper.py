from datetime import datetime

def create_msg(*args):
    now = datetime.now()
    return now.strftime('[%Y/%m/%d %H:%M:%S]{}'.format('params => ')) + ' '.join(args)