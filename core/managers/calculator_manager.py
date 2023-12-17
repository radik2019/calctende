#!/usr/bin/python3


class FixedFoldManager:
    ASSE_DA_STIRO = 121
    PRINTED_WIDTH = 30
    APP_NAME = ' '.join(list("PIEGA FISSA")).center(PRINTED_WIDTH, ' ')

    def __init__(self, fold_approximated, interior_fold, awning_measure, cloth_measure, *args):
        self.cloth_measure = cloth_measure
        self.awning_measure = awning_measure
        self.fold_approximated = fold_approximated
        self.interior_fold = interior_fold
        self.fold_count = None
        self.fold_interval = None
        self.effective_fold = None
        self.asseFlag = True
        self.ready_measure_list = []
        self.asseDaStiroMisure = None
        self.exitFlag = True

    def error_message(self):
        remaning_cloth = self.cloth_measure - ((self.interior_fold * 2) + self.awning_measure)
        if remaning_cloth < self.fold_approximated + 2:
            return "misura della stoffa troppo piccola per il tendaggio scelto"
    def set_fold(self) -> tuple:
        self.effective_fold = self.awning_measure / (self.awning_measure // self.fold_approximated)

    def set_fold_count(self):
        self.fold_count = self.awning_measure / self.effective_fold

    def set_fold_range(self):
        stoffa_rimanente = self.cloth_measure - ((self.interior_fold * 2) + self.awning_measure)
        self.fold_interval = stoffa_rimanente / (self.fold_count - 1)

    def __set_ready_measure_list(self):
        ironing_board = True
        count = 0
        i = 0
        while i < (self.cloth_measure - self.interior_fold * 2):
            i += self.effective_fold
            self.ready_measure_list.append({'distance':round(i, 2),
                                            'interval': self.effective_fold ,
                                            'type': 'piega',
                                            'color':'#d7c11f'})
            i += self.fold_interval
            self.ready_measure_list.append({'distance':round(i, 2),
                                            'interval': self.fold_interval ,
                                            'type': 'intervallo',
                                            'color':'#d7c1ff'})

    def get_measure_list(self):
        error = self.error_message()
        if not error:
            self.set_fold()
            self.set_fold_count()
            self.set_fold_range()
            self.__set_ready_measure_list()
            return self.ready_measure_list


if __name__ == "__main__":
    pf = FixedFoldManager(8, 8, 122, 345)
    print(pf.get_measure_list())
