from flask import Flask, render_template, request
import PIL.Image as Image
import torch
import torchvision.transforms as transforms

app = Flask(__name__)

classes = [
    'not threat',
    'threat'
]

mean = [0.2842, 0.3798, 0.4523]
std  = [0.2231, 0.1942, 0.1880]

image_transforms = transforms.Compose([transforms.Resize((224, 224)),
                                transforms.ToTensor(),
                                transforms.Normalize(torch.Tensor(mean), torch.Tensor(std))])

model = torch.load('website/best_model.pth')

def classify(model, image_transforms, image_path, classes):
    model = model.eval()
    image = Image.open(image_path)
    image = image_transforms(image).float()
    image = image.unsqueeze(0)
 
    output = model(image)
    _, predicted = torch.max(output.data, 1)
    
    return (classes[predicted.item()])

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "This is an Image Recognition Project built by Prathamesh Pandey, Jainam Jain, Kashyap Jethwa and Jay Kore 🗿"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "website/static/" + img.filename	
		display_path = "static/" + img.filename
		img.save(img_path)

		p = classify(model, image_transforms, img_path, classes)
	print(img_path)
	return render_template("index.html", prediction = p, new_image = display_path)





if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
 
