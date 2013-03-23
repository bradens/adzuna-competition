import data_io
import convert_to_vw as c
import dummy_column as dc


def main():
	print("Converting training data to vw format")
	c.convert_to_vw("../data/Train.csv", "../results/train.vw")

	print("Adding dummy columns to validate data")
	dc.add_dummy_columns("../data/Valid.csv", "../data/Valid_Dummy.csv")

	print("Converting validate data to vw format")
	c.convert_to_vw("../data/Valid_Dummy.csv", "../results/valid.vw")

if __name__=="__main__":
	main()