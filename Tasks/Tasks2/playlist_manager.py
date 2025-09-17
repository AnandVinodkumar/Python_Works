playlist = ["songA", "songB", "songC", "songD"]

playlist.insert(0,"intro")

print(playlist)

playlist.append("outro")

print(playlist)

playlist.remove("songB")

print(playlist)

playlist.reverse()

playlist1 = playlist.copy()

print(playlist1)