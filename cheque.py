def ler_cheque(extenso):

	partes = extenso.split()

	if partes[0] == "um":
		return 1

	if partes[0] == "dois":
		return 2

	#if extenso == "um real e um centavo":
	#	return 1.1

