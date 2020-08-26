scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    info.changeScoreBy(1)
    music.powerUp.playUntilDone()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.buttonTealDepressed, function (sprite, location) {
    game.over(true, effects.hearts)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile1, function (sprite, location) {
    game.over(false)
})
let Fish = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . c c c c . . . . 
    . . . . . . c c d d d d c . . . 
    . . . . . c c c c c c d c . . . 
    . . . . c c 4 4 4 4 d c c . . . 
    . . . c 4 d 4 4 4 4 4 1 c . c c 
    . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
    . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
    f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
    f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
    f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
    . f 4 4 4 4 1 c 4 f 4 d f f f f 
    . . f f 4 d 4 4 f f 4 c f c . . 
    . . . . f f 4 4 4 4 c d b c . . 
    . . . . . . f f f f d d d c . . 
    . . . . . . . . . . c c c . . . 
    `, SpriteKind.Player)
controller.moveSprite(Fish, 150, 150)
scene.setBackgroundColor(9)
tiles.setTilemap(tiles.createTilemap(hex`1000100001010101010101010101010101010101060202020201010404040101020202070101010602010104040401010201010101010106020101040404010102010101010101010201010202020101020101010101050202010102010202020201010101010202050101020101020201010101010102010101010201010201010101010101020202020202010102010101010101010601010101010101020101010101010106010101010102020201010101010104040102020202020101010204040101040401020101010101010602020201010101010201010101010105020102010101010102020202020202020201020101010101010101010101010101010301`, img`
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
    . . . . . 2 2 . . . 2 2 . . . . 
    2 2 2 . . 2 2 . . . 2 2 . 2 2 2 
    . . 2 . . 2 2 . . . 2 2 . 2 . . 
    . 2 2 2 . 2 2 . . . 2 2 . 2 . . 
    . 2 . . . 2 2 . 2 . . . . 2 . . 
    . 2 . . . 2 2 . 2 2 . . 2 2 . . 
    . 2 . 2 2 2 2 . 2 2 . 2 2 . . . 
    . 2 . . . . . . 2 2 . 2 . . . . 
    . 2 . 2 2 2 2 2 2 2 . 2 . . . . 
    2 2 . 2 2 2 2 2 . . . 2 2 2 2 2 
    2 . . 2 . . . . . 2 2 2 . . . 2 
    2 . . 2 . 2 2 2 2 2 2 . . . . 2 
    2 2 2 2 . 2 2 2 2 2 2 . . 2 . 2 
    . . . 2 . . . . . . . . . 2 . 2 
    . . . 2 2 2 2 2 2 2 2 2 2 2 . 2 
    `, [myTiles.transparency16,sprites.builtin.coral0,sprites.dungeon.hazardWater,sprites.dungeon.buttonTealDepressed,sprites.dungeon.hazardLava0,sprites.dungeon.chestClosed,myTiles.tile1,sprites.dungeon.buttonPink], TileScale.Sixteen))
tiles.placeOnRandomTile(Fish, sprites.dungeon.buttonPink)
scene.cameraFollowSprite(Fish)
info.startCountdown(20)
