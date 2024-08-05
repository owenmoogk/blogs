import os
import json
import frontmatter

def process_markdown_files(json_file):

	files = [os.path.join("blogs", file) for file in os.listdir("blogs") if os.path.isfile(os.path.join("blogs", file))]
	data = []
	for md_file in files:
		try:
			with open(md_file, 'r', encoding='utf-8') as f:
				post = frontmatter.loads(f.read())
		except Exception as e:
			print(f"Error processing {md_file}: {e}")
			continue

		title = post.get("title", "Untitled")
		tags = post.get("tags", [])
		date = post.get("date")
		entry = {
			"date": date,
			"title": title,
			"tags": tags,
			"file_path": "https://owenmoogk.github.io/blogs/" + md_file,
			"file_name": md_file.replace(".md", "")
		}
		data.append(entry)

	# Write updated data back to the JSON file
	with open(json_file, 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=4)


if __name__ == "__main__":
	output_json = "./metadata.json"  # JSON file to be updated
	process_markdown_files(output_json)