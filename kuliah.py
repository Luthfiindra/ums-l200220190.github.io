from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):
    @step
    def start(self):
        print("Memulai proses mengikuti kuliah Informatika.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        print("Pembayaran SPP dilakukan.")
        self.next(self.kuliah)

    @step
    def kuliah(self):
        print("Mengikuti kuliah.")
        self.next(self.mengerjakan_tugas)

    @step
    def mengerjakan_tugas(self):
        print("Mengerjakan tugas kuliah.")
        self.next(self.akhir)

    @step
    def akhir(self):
        print("Mendapatkan nilai akhir mata kuliah.")
        self.final_value = "A"
        print(f"Nilai akhir: {self.final_value}")
        self.next(self.end)

    @step
    def end(self):
        print("Proses mengikuti kuliah Informatika selesai.")

if __name__ == '__main__':
    KuliahInformatikaFlow()