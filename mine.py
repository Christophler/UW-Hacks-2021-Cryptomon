
async def mine(message, discord, mineInt, numGraphicCards, random):
  mineInt = random.randint(1,100)
  # Dogecoin encounter
  if (mineInt <= 75):
    await message.channel.send('You found **Dogecoin**! \n', file=discord.File('dogecoin.jpg')) # REQUIRES THE 'dogecoin.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')

  # Etherium encounter
  if ((mineInt <= 99) and (mineInt > 75)):
    await message.channel.send('You found **Ethereum**! \n', file=discord.File('ethereum.jpg')) # REQUIRES THE 'ethereum.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')

  # Bitcoin encounter
  if (mineInt == 100):
    await message.channel.send('You found **Bitcoin**!!! \n', file=discord.File('bitcoin.jpg')) # REQUIRES THE 'dogecoin.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')
  
  await message.channel.send('Use the **$validate** command to try to catch the crypto!')
  
  encounter = True

  return (encounter, mineInt)
