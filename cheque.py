inteiros = {
	"um": 1,
	"dois": 2,
	"tres": 3,
	"quatro": 4,
	"cinco": 5,
	"treze": 13,
	"quinze": 15,
	"vinte": 20,
	"cento": 100,
	"cem": 100
}

def ler_cheque(extenso):

	partes = extenso.split()

	if len(partes) > 2 and partes[3] == "e":
		valor = ler_numero(partes[0]) + ler_numero(partes[2]) + ler_numero(partes[4])
	elif partes[1] == "e":
		valor = ler_numero(partes[0]) + ler_numero(partes[2])
	else:
		valor = ler_numero(partes[0])

	return valor


def ler_numero(numeroStr):
	return inteiros[numeroStr]