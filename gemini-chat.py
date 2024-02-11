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
    parser.add_argument('-i', '--image', dest='image', default=None, 
                        help='pass an image as part of a query')
    args = parser.parse_args()

    if args.image is not None:
        img = PIL.Image.open(args.image)
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([" ".join(args.query), img])
    else:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(" ".join(args.query))
    print(response.text)

    if args.candidates:
        print(response.candidates)

if __name__ == "__main__":
    main()
