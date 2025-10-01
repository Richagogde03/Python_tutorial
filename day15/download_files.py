# import multiprocessing
import requests
import concurrent.futures


def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished  Downloading {name}")
    return name


if __name__ == "__main__":
    urls = "https://picsum.photos/2000/3000"
    # pros = []
    # for i in range(35):
    #     # downloadFile(urls, i)
    #     p = multiprocessing.Process(target=downloadFile, args=[urls, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [urls for i in range(20)]
        l2 = [i for i in range(20)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)
