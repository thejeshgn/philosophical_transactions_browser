
#Really bad code dont judge me. I wanted it quick n easy
import os
import glob
import sqlite3
JSTOR_01_PhilTrans_path = '/home/thej/Documents/present/JSTOR_01_PhilTrans'
path_to_meta_docs = JSTOR_01_PhilTrans_path+'/PRE_1923_METADATA/'
metadata_folders = ['00','01','02','03','04','05','06','07','08', '09','10','11']
conn = sqlite3.connect("/media/truecrypt5/code/jstor_philtrans_browser/metadata.sqlite")

for meta_folder in metadata_folders:
	folder_path = glob.glob(path_to_meta_docs+meta_folder+"/*.txt")
	for file_path in folder_path:
		inputs = []
		ID = os.path.basename(file_path)[:-4]
		TY =""
		T1  =""
		JF  =""
		VL  =""
		SP  =""
		EP  =""
		PY  =""
		UR  =""
		M3  =""
		AU  =""
		ER   =""
		
		with open(file_path) as f:
			file_content = f.readlines()
			for content in file_content:
				if content.startswith("TY  - ") :
					TY = content[6:].strip()
				if content.startswith("T1  - ") :
					T1 = content[6:].strip()
				if content.startswith("JF  - ") :
					JF = content[6:].strip()
				if content.startswith("VL  - ") :
					VL = content[6:].strip()
				if content.startswith("SP  - ") :
					SP = content[6:].strip()
				if content.startswith("EP  - ") :
					EP = content[6:].strip()
				if content.startswith("PY  - ") :
					PY = content[6:].strip()
				if content.startswith("UR  - ") :
					UR = content[6:].strip()
				if content.startswith("M3  - ") :
					M3 = content[6:].strip()
				if content.startswith("AU  - ") :
					AU = content[6:].strip()
				if content.startswith("ER  - ") :
					ER = content[6:].strip()

		inputs.append(ID)
		inputs.append(TY)
		inputs.append(T1)
		inputs.append(JF)
		inputs.append(VL)
		inputs.append(SP)
		inputs.append(EP)
		inputs.append(PY)
		inputs.append(UR)
		inputs.append(M3)
		inputs.append(AU)
		inputs.append(ER)
		inputs.append(meta_folder)
		print inputs
		conn.execute('INSERT INTO documents(ID, TY ,T1  ,JF  ,VL  ,SP  ,EP  , PY  ,UR  ,M3  ,AU  ,ER,FOLDER ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', inputs)
		conn.commit()
conn.close()