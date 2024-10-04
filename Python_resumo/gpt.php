

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['croppedImage'])) {
        $file = $_FILES['croppedImage'];
        $uploadDir = 'uploads/';
        $fileName = uniqid() . '.jpg';  // Gera um nome único para a imagem
        $uploadPath = $uploadDir . $fileName;

        // Verifica se o diretório de upload existe, se não, cria
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        // Move o arquivo carregado para o diretório de destino
        if (move_uploaded_file($file['tmp_name'], $uploadPath)) {
            echo 'Imagem carregada com sucesso!';
        } else {
            echo 'Falha ao carregar a imagem.';
        }
    } else {
        echo 'Nenhuma imagem foi enviada.';
    }
} else {
    echo 'Método de solicitação inválido.';
}

// https://bitnami.com/stacks?utm_source=bitnami&utm_medium=installer&utm_campaign=XAMPP%2BInstaller
?>


<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Upload e Recorte de Imagem</title>
  <!-- Inclua o CSS do Cropper.js -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.css" rel="stylesheet">
  <style>
    /* Estilo para a área de pré-visualização */
    .img-container {
      max-width: 100%;
      max-height: 500px;
    }
    img {
      display: block;
      max-width: 100%;
    }
  </style>
</head>
<body>

<div class="img-container">
  <img id="image" src="" alt="Imagem para recortar">
</div>
<input type="file" id="inputImage" accept="image/*">
<button id="cropButton">Recortar e Enviar</button>

<!-- Inclua o JS do Cropper.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.js"></script>
<script>
  // Inicializa o Cropper.js
  let cropper;
  const image = document.getElementById('image');
  const inputImage = document.getElementById('inputImage');
  const cropButton = document.getElementById('cropButton');

  inputImage.addEventListener('change', function(event) {
    const files = event.target.files;
    if (files && files.length > 0) {
      const reader = new FileReader();
      reader.onload = function(e) {
        image.src = e.target.result;
        if (cropper) {
          cropper.destroy(); // Destroi o cropper existente antes de criar um novo
        }
        cropper = new Cropper(image, {
          aspectRatio: 1, // Proporção quadrada 1:1
          viewMode: 1,
          autoCropArea: 1,
        });
      };
      reader.readAsDataURL(files[0]);
    }
  });

  cropButton.addEventListener('click', function() {
    if (cropper) {
      const canvas = cropper.getCroppedCanvas({
        width: 300,
        height: 300,
      });
      canvas.toBlob(function(blob) {
        const formData = new FormData();
        formData.append('croppedImage', blob, 'cropped.jpg');

        // Envia a imagem recortada ao servidor
        fetch('upload.php', {
          method: 'POST',
          body: formData,
        }).then(response => {
          return response.text();
        }).then(data => {
          console.log(data); // Exibe a resposta do servidor
        }).catch(error => {
          console.error('Erro:', error);
        });
      }, 'image/jpeg');
    }
  });
</script>
</body>
</html>


