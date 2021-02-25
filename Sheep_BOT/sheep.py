import discord
#import asyncio
import random

#from discord.ext.commands.converter import RoleConverter
import sheep_run
from discord.ext import commands

#client = discord.Client()
token = sheep_run.run()                             # Insira aqui o Token do BOT
client = commands.Bot(command_prefix='!')

msg_id = None
msg_user = None

games = random.choice(['League of Legends', 'Minecraft', 'D&D - 5e', 'VALORANT'])
opiniao = (['Aí é foda..', 'Que fita..', 'Têm que ver isso ai', 'Béééé', 
'Mesmo sendo um BOT sei que isso ai é coisa de arromb@$*', 'Se olhar bem da pra notar o erro',
'Humanos, tsc tsc...\n\n\n\nˢᵒ ⁿᵃᵒ ˢᵃᵒ ᵖᶦᵒʳᵉˢ ᑫᵘᵉ ᵉˡᶠᵒˢ...', 'A ideia é boa, pena que é ruim'])
numeros = (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

@client.event
async def on_ready():
    print(f'Ligado')
    '''await client.change_presence(activity=discord.activities(name=games,type=3))'''
# foi retirado o activities
@client.event
async def on_message(message):

    id = client.get_guild(sheep_run.guild())            # Insira aqui o ID da guild (a qual o bot esta inserido)

    if message.content.lower().startswith('🐑'):
        await message.channel.send(':sheep:')
    
    if message.content.lower().startswith('benjamin'):
        await message.channel.send('_Ai meu deus_')
    
    if message.content.lower().startswith('!opinião'):
        await message.channel.purge(limit=1)
        await message.channel.send(random.choice(opiniao))

    if message.content.lower().startswith('oi'):
        await message.channel.send(f'Olá, **{message.author.mention}**')
        if message.author.id == sheep_run.eu():                             # Insira aqui o seu ID
            if games == 'League of Legends':
                await message.channel.send('Não estou podendo conversar, conseguiram feedar uma Yummi ADC')
            elif games == 'Minecraft':
                await message.channel.send('...')
            elif games == 'D&D - 5e':
                await message.channel.send('Compreendo que se trata de imaginação, mas como alguém consegue andar com 1000po no bolso?')
            elif games == 'VALORANT':
                await message.channel.send('O que caral&$# é brocar???')
    
    if message.content.lower().startswith('!clear'):
        deletar = 0
        user = message.author.mention
        await message.channel.send(f'{user} deletar quantas mensagens?')
        if message.author == user:
            if user.message.content.startswith(int):
                print('Esse aqui passou')    
                deletar = int(message.content)
                await message.channel.purge(limit=deletar)

    if message.content == '!users':
        await message.channel.purge(limit=1)
        await message.channel.send(f'Total de usuários: {id.member_count}')
        # NoneType no member_count
    
    if message.content.lower().startswith('!d20'):
        maluco = f'{message.author}'
        d20_1 = discord.Embed(
            title=maluco, color= 0xa3fefe, description=f'Seu resultado foi: **{random.randint(1, 20)}**'
        )
        #d20 = message.channel.send(f'**{message.author.mention}**\nSeu resultado foi: **{random.randint(1, 20)}**')
        await message.channel.purge(limit=1)
        await message.channel.send(embed=d20_1)

    if message.content.lower().startswith('!init_list'):
        await message.channel.purge(limit=1)
        await message.channel.send('Lista iniciada!')

    if message.content.lower().startswith('!classe'):
        await message.channel.purge(limit=1)
        classes = discord.Embed(
            title='**Escolha sua classe!**', 
            color= 0x6699ff, 
            description=
            'Bárbaro = :angry:   | Bardo = :guitar:    | Bruxo = :jack_o_lantern:\n'
            'Clérigo = :helmet_with_cross:    | Druida = :herb:   | Feiticeiro = :boom:\n'
            'Guerreiro = :shield: | Ladino = :dagger:  | Mago = :mage:\n'
            'Monge = :shinto_shrine:    | Paladino = :church: | Patrulheiro = :archery:\n'
            '-=-= Mestre = :earth_americas: =-=-\n\n'
            '_**ATENÇÃO**, antes de escolher uma classe, '
            'certifique se de ter mudado o seu apelido para o do seu personagem_'
            )
        definir_classes = await message.channel.send(embed=classes)
        await definir_classes.add_reaction("😠")
        await definir_classes.add_reaction("🎸")
        await definir_classes.add_reaction("🎃")
        await definir_classes.add_reaction("⛑")
        await definir_classes.add_reaction("🌿")
        await definir_classes.add_reaction("💥")
        await definir_classes.add_reaction("🛡")
        await definir_classes.add_reaction("🗡")
        await definir_classes.add_reaction("🧙")
        await definir_classes.add_reaction("⛩")
        await definir_classes.add_reaction("⛪")
        await definir_classes.add_reaction("🏹")
        await definir_classes.add_reaction("🌎")

        id_sheep_msg = message.id
        id_sheep_bot = sheep_run.Sheep_ID_Bot()

        @client.event
        async def on_raw_reaction_add(payload):
            if message.id == id_sheep_msg:
                if payload.user_id != id_sheep_bot:
                    guild_id = payload.guild_id
                    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    #nome = member.nick

                    '''if payload.emoji.name == '😠':
                        role = discord.utils.get(guild.roles, name='Bárbaro')
                        await member.edit(nick=member.nick+'😠')
                    elif payload.emoji.name == '🎸':
                        role = discord.utils.get(guild.roles, name='Bardo')
                        await member.edit(nick=member.nick+'🎸')
                    elif payload.emoji.name == '🎃':
                        role = discord.utils.get(guild.roles, name='Bruxo')
                        await member.edit(nick=member.nick+'🎃')
                    elif payload.emoji.name == '⛑':
                        role = discord.utils.get(guild.roles, name='Clérigo')
                        await member.edit(nick=member.nick+'⛑')
                    elif payload.emoji.name == '🌿':
                        role = discord.utils.get(guild.roles, name='Druida')
                        await member.edit(nick=member.nick+'🌿')
                    elif payload.emoji.name == '💥':
                        role = discord.utils.get(guild.roles, name='Feiticeiro')
                        await member.edit(nick=member.nick+'💥')
                    elif payload.emoji.name == '🛡':
                        role = discord.utils.get(guild.roles, name='Guerreiro')
                        await member.edit(nick=member.nick+'🛡')
                    elif payload.emoji.name == '🗡':
                        role = discord.utils.get(guild.roles, name='Ladino')
                        await member.edit(nick=member.nick+'🗡')
                    elif payload.emoji.name == '🧙':
                        role = discord.utils.get(guild.roles, name='Mago')
                        await member.edit(nick=member.nick+'🧙')
                    elif payload.emoji.name == '⛩':
                        role = discord.utils.get(guild.roles, name='Monge')
                        await member.edit(nick=member.nick+'⛩')
                    elif payload.emoji.name == '⛪':
                        role = discord.utils.get(guild.roles, name='Paladino')
                        await member.edit(nick=member.nick+'⛪')
                    elif payload.emoji.name == '🏹':
                        role = discord.utils.get(guild.roles, name='Patrulheiro')
                        await member.edit(nick=member.nick+'🏹')
                    elif payload.emoji.name == '🌎':
                        role = discord.utils.get(guild.roles, name='Mestre')
                        await member.edit(nick=member.nick+'🌎')'''
            # Foi retirado o edit (na real nao sei, mas esta dando nonetype)
                    if role is not None:
                        if member is not None:
                            await member.add_roles(guild.role)
                            print(f'{member} adicionou a Classe {role.name}')
                        else:
                            print(f'Erro ao adicionar a classe para {member}')

        @client.event
        async def on_raw_reaction_remove(payload):
            #nome = str(discord.Member.nick)
            if message.id == id_sheep_msg:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                '''nome = member.nick'''
                # Foi retirado o nick (na real nao sei, mas esta dando nonetype)
                
                if payload.emoji.name == '😠':
                    role = discord.utils.get(guild.roles, name='Bárbaro')
                    await member.edit(nick=nome.replace("😠",""))
                elif payload.emoji.name == '🎸':
                    role = discord.utils.get(guild.roles, name='Bardo')
                    await member.edit(nick=nome.replace("🎸",""))
                elif payload.emoji.name == '🎃':
                    role = discord.utils.get(guild.roles, name='Bruxo')
                    await member.edit(nick=nome.replace("🎃",""))
                elif payload.emoji.name == '⛑':
                    role = discord.utils.get(guild.roles, name='Clérigo')
                    await member.edit(nick=nome.replace("⛑",""))
                elif payload.emoji.name == '🌿':
                    role = discord.utils.get(guild.roles, name='Druida')
                    await member.edit(nick=nome.replace("🌿",""))
                elif payload.emoji.name == '💥':
                    role = discord.utils.get(guild.roles, name='Feiticeiro')
                    await member.edit(nick=nome.replace("💥",""))
                elif payload.emoji.name == '🛡':
                    role = discord.utils.get(guild.roles, name='Guerreiro')
                    await member.edit(nick=nome.replace("🛡",""))
                elif payload.emoji.name == '🗡':
                    role = discord.utils.get(guild.roles, name='Ladino')
                    await member.edit(nick=nome.replace("🗡",""))
                elif payload.emoji.name == '🧙':
                    role = discord.utils.get(guild.roles, name='Mago')
                    await member.edit(nick=nome.replace("🧙",""))
                elif payload.emoji.name == '⛩':
                    role = discord.utils.get(guild.roles, name='Monge')
                    await member.edit(nick=nome.replace("⛩",""))
                elif payload.emoji.name == '⛪':
                    role = discord.utils.get(guild.roles, name='Paladino')
                    await member.edit(nick=nome.replace("⛪",""))
                elif payload.emoji.name == '🏹':
                    role = discord.utils.get(guild.roles, name='Patrulheiro')
                    await member.edit(nick=nome.replace("🏹",""))
                elif payload.emoji.name == '🌎':
                    role = discord.utils.get(guild.roles, name='Mestre')
                    await member.edit(nick=nome.replace("🌎",""))

                if discord.role is not None:
                    if member is not None:
                        await member.remove_roles(role)
                        print(f'{member} abandonou a Classe {role.name}')
                    else:
                        print(f'Erro ao remover a classe de {member}')

    if message.content.lower().startswith('!sneak'):
        await message.channel.purge(limit=1)
        snk_att = discord.Embed(
            title = 'Ataque Furtivo',
            color = 0x4f4f4f,
            description =
            'A partir do 1º nível, você sabe como atacar sutilmente e explorar a distração de seus inimigos.\n'
            'Uma vez por turno, você pode adicionar 1d6 nas jogadas de dano contra qualquer criatura que acertar, **desde que '
            'tenha vantagem nas jogadas de ataque**. O ataque deve ser com uma arma de acuidade ou à distância. '
            '**Você não precisa ter vantagem nas jogadas de ataque se outro inimigo do seu alvo estiver a 1,5 metro de distância dele**, desde que '
            'este inimigo não esteja incapacitado **e você não tenha desvantagem nas jogadas de ataque**. '
            'A quantidade de dano extra aumenta conforme você ganha níveis nessa classe, como mostrado na coluna Ataque Furtivo da tabela O Ladino.'
        )
        await message.channel.send(embed=snk_att)
client.run(token)
