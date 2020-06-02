import xmltodict

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
