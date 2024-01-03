from PIL import Image
import os

def convert_to_grayscale(input_folder, output_folder):
    # Giriş klasöründeki tüm dosyaları al
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Çıkış klasörünü oluştur
    os.makedirs(output_folder, exist_ok=True)

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_bw.jpg")

        # Resmi aç ve siyah beyaz formatına dönüştür
        with Image.open(input_path).convert('L') as img:
            img.save(output_path, "JPEG")

def rename_files_with_prefix(input_folder, prefix):
    # Giriş klasöründeki tüm dosyaları al
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Dosyaları sırala
    files.sort()

    # Dosyaları yeni isimlendirme şekliyle yeniden adlandır
    for index, file_name in enumerate(files, start=1):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{prefix}{index}{file_extension}"
        
        # Dosyayı taşı ve yeniden adlandır
        old_path = os.path.join(input_folder, file_name)
        new_path = os.path.join(input_folder, new_file_name)
        os.rename(old_path, new_path)
        print(f"{file_name} -> {new_file_name}")

if __name__ == "__main__":
    input_folder = r"C:\Users\ysfmr\Downloads\aircraft_cascade\negatif_output"  # Resimlerin bulunduğu klasörü belirtin
    output_folder = r"C:\Users\ysfmr\Downloads\aircraft_cascade\klasor_negative"  # Siyah beyaz olarak kaydedilecek resimlerin klasörünü belirtin
    prefix = "sivil"  # Yeniden adlandırma için önek belirtin

    convert_to_grayscale(input_folder, output_folder)
    rename_files_with_prefix(output_folder, prefix)
