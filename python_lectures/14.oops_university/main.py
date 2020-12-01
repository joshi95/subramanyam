from batch.batch import Batch
from university.attainu import Attainu

if __name__ == '__main__':

    attainu = Attainu("attainu", "Noida-128", "A")

    print("how many batches do you want insert")
    n = int(input())

    while n > 0:
        print("please enter the batch name")
        batch_name = input()
        print("please enter the no of students")
        strength = int(input())

        batch = Batch(batch_name, strength)
        attainu.add_batch(batch)
        n -= 1

    attainu.print_all_batches()
    # subramanyam = Batch("subramanyam", 100)
    # attainu.add_batch(subramanyam)
    #
    # cv_raman = Batch("cv_raman", 50)
    # attainu.add_batch(cv_raman)
    #
    # aryabhatta = Batch("aryabhatta", 10)
    # attainu.add_batch(aryabhatta)


