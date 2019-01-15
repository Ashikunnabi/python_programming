import webbrowser

def main():
    print("Opening Favorite Sites.")
	
    with open("_32_site_list.txt") as favorite_sites:
        try:
            for num, url in enumerate(favorite_sites):
                webbrowser.open_new_tab(url.strip())
                print("\n"+url)
        except Exception as e:
            print(e)
    print("\nEnjoy")

if __name__ == "__main__": main()
