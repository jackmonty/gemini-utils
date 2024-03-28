import argparse
import google.generativeai as genai
import PIL.Image


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='Pass queries to Gemini Pro via API')
    parser.add_argument('query', nargs='*', default="", 
                        help='the query for Gemini Pro')
    parser.add_argument('-c', '--candidates', dest='candidates', action='store_true',
                        default=False, help='display all candidates if more than one')
    parser.add_argument('-m', '--list-models', dest='list_models', action='store_true',
                        default=False, help='display all models available')
    parser.add_argument('-i', '--image', dest='image', default=None, 
                        help='pass an image as part of a query')
    args = parser.parse_args()

    # Construct query if present
    query = []
    if args.query != "":
        query.append(" ".join(args.query))
    if args.image is not None:
        img = PIL.Image.open(args.image)
        model = genai.GenerativeModel('gemini-pro-vision')
        query.append(img)
    else:
        model = genai.GenerativeModel('gemini-pro')
    if len(query) > 0:
        response = model.generate_content(query)
        print(response.text)

    # Print candidates JSON if requested
    if args.candidates:
        if args.query != "":
            print(response.candidates)
        else:
            print("To list candidates, enter a query")

    # List models if requested
    if args.list_models:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

if __name__ == "__main__":
    main()
