# agent for wallet

def saldo(asset):
	asset = 'agent/wallet-'+asset+'.txt'
	wallet = open(asset, 'r') 
	return wallet.read()

def wallet(asset, amount, status):
	asset = 'agent/wallet-'+asset+'.txt'

	wallet = open(asset, 'r')
	if status == 'in':
		saldo = int(wallet.read()) + amount
	else:
		saldo = int(wallet.read()) - amount
		if saldo < 0:
			saldo = 0
	wallet = open(asset, 'w')
	wallet.write(str(saldo))
	wallet.close()
	return saldo