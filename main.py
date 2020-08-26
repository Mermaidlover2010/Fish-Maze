def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    info.change_score_by(1)
    music.power_up.play_until_done()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    game.over(True, effects.hearts)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.button_teal_depressed,
    on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile1, on_overlap_tile4)

Fish = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(Fish, 150, 150)
scene.set_background_color(9)
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100001010101010101010101010101010101060202020201010404040101020202070101010602010104040401010201010101010106020101040404010102010101010101010201010202020101020101010101050202010102010202020201010101010202050101020101020201010101010102010101010201010201010101010101020202020202010102010101010101010601010101010101020101010101010106010101010102020201010101010104040102020202020101010204040101040401020101010101010602020201010101010201010101010105020102010101010102020202020202020201020101010101010101010101010101010301
        """),
        img("""
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
        """),
        [myTiles.transparency16,
            sprites.builtin.coral0,
            sprites.dungeon.hazard_water,
            sprites.dungeon.button_teal_depressed,
            sprites.dungeon.hazard_lava0,
            sprites.dungeon.chest_closed,
            myTiles.tile1,
            sprites.dungeon.button_pink],
        TileScale.SIXTEEN))
tiles.place_on_random_tile(Fish, sprites.dungeon.button_pink)
scene.camera_follow_sprite(Fish)
info.start_countdown(20)