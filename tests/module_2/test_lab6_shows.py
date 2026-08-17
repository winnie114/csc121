from module_2 import lab6_shows

def test_should_print_cleaned_and_title_cased_show_names(capsys):
    assert hasattr(lab6_shows, "main"), "shows.py has no main() function. File may be blank"
    lab6_shows.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "Avatar: The Last Airbender, Ben 10, Arthur, Spongebob Squarepants, "
        "Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family\n"
    )
