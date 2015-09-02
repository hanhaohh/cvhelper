# from config import URL_DOWNLOAD_LIST, URL_VISITED_FILE_LIST, DOWLOAD_THREAD_POOL_SIZE, ANAYLIZER_THREAD_POOL_SIZE
from time import sleep
from mult_proc_linkedin import *
if __name__ == '__main__':
    output = "linkedin.list"
    term = "data"
    queue = Queue(config.QUEUE_SIZE)
    for i in xrange(1,config.QUEUE_SIZE+1,1):
        queue.put(i)

    #start the threads
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    threads = []
    process_id  = 1
    for tName in threadList:
        thread = Linkedin("hanhaohh@126.com", "hanhaohh",queue =queue,thread_name=tName,thread_id = process_id,term=term,out=output)
        threads.append(thread)
        process_id = process_id+1
    for i in threads:
        i.start()
    # wait until the input queue is empty   
    while not queue.empty():
        pass
    for i in threads:
        i.stop() 
    # thread_pool_download = []
    # thread_pool_link_extract = []

    # ##################### create threads #####################
    # for i in range(DOWLOAD_THREAD_POOL_SIZE):
    #     new_downloader = Downloader(thread_num=i)
    #     thread_pool_download.append(new_downloader)

    # for i in range(ANAYLIZER_THREAD_POOL_SIZE):
    #     new_link_extractor = LinkExtractor(base_url=base_url)
    #     thread_pool_link_extract.append(new_link_extractor)
    # ##################### End #####################

    # ##################### start threads #####################
    # for i in range(DOWLOAD_THREAD_POOL_SIZE):
    #     thread_pool_download[i].start()

    # for i in range(ANAYLIZER_THREAD_POOL_SIZE):
    #     thread_pool_link_extract[i].start()
    # ##################### End #####################
