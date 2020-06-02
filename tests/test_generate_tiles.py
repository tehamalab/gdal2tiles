import xmltodict
from PIL import Image

from gdal2tiles import generate_tiles


def test_basic(data, tmp_path):
    """Basic sanity check"""
    input_file = data / 'simple.tiff'
    output_dir = tmp_path / 'tiles'
    output_dir.mkdir()

    generate_tiles(str(input_file), str(output_dir))

    # ensure a tilemapresource.xml was created
    with (output_dir / 'tilemapresource.xml').open('r') as f:
        tiles_info = xmltodict.parse(f.read())
    assert 'TileMap' in tiles_info

    # ensure some PNG images were created
    tiles_created = list(output_dir.rglob("*.png"))
    assert len(tiles_created) > 0


def test_tile_size(data, tmp_path):
    """
    Test if tiles are generated with correct size based on ``tile_size`` parameter
    """
    input_file = data / 'simple.tiff'
    output_dir = tmp_path / 'tiles'

    sizes = [128, 256, 512]

    for size in sizes:
        generate_tiles(str(input_file), str(output_dir), tile_size=size)
        tiles_dir = output_dir / str(size)
        for tile_path in tiles_dir.rglob("*.png"):
            tile_image = Image.open(tile_path)
            tile_width, tile_height = tile_image.size
            assert tile_width == size
            assert tile_height == size
