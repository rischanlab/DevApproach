# -*- coding: utf-8 -*-
from devapproach import devApproach
from student import data

if __name__ == "__main__":
    db,table,data_set = data()

    top_k = 10

    framework = devApproach(db,data_set,table,top_k)
    framework.main()