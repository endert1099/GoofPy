import goofpy

# define important things
c = goofpy.Creator()

player = goofpy.Player(0, 0, 0, 0, 90)
game = goofpy.Game()
game.initEngine()

# define goof objects
Objs = [
    goofpy.goof(0, "TestMeta"),
    goofpy.goof(1, "OtherMeta"),
    goofpy.goof(2, "FinalMeta"),
    goofpy.goof(3, "TestMeta"),
]

# convert goof objects

gameObjs = [
    c.new3D(10, 0, 0, ["scalex", 0.5, "scaley", 1, "scalez", 3, "collider", True, "isActive", True, "isInvis", False])
]
GameObjData = []
for obj in gameObjs:
    GameObjData.append(obj.formatData())

# run game
def gameF():
    if game.keyPressed("w"):
        player.move(1)
    if game.keyPressed("s"):
        player.move(-1)
    if game.keyPressed("a"):
        player.turn(-1)
    if game.keyPressed("d"):
        player.turn(1)

    player.x = round(player.x, 2)
    player.y = round(player.y, 2)

    print(f"Player is at {player.x}, {player.y}, {player.z}, with a rotation of {player.facing}")
    for i in range(len(gameObjs)):
        gObj = gameObjs[i]
        data = GameObjData[i]

        if player.isColliding(gObj):
            raise SystemExit("Dead!")

game.run(gameF, 60)
game.engine.quit()
# print(player.isColliding(goofGameObj))
