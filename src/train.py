import data_io
import convert_to_vw as c
import dummy_column as dc


def main():
	print("Converting training data to vw format")
	c.convert_to_vw("../data/Train.csv", "../results/train.vw")

	print("Adding dummy column to validate data")
	dc.add_dummy_column("../data/Valid.csv", "../data/Valid_Dummy.csv")



if __name__=="__main__":
	main()