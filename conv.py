import json
import ast


def convert_tokenizer_json(input_file='tokenizer.json', output_file='tokenizer_fixed.json'):
    # Baca file tokenizer
    with open(input_file, 'r', encoding='utf-8') as f:
        tokenizer_content = f.read()

    # Hapus escape characters dan tanda kutip tambahan
    tokenizer_content = tokenizer_content.replace('\\"', '"')

    # Gunakan ast.literal_eval untuk mengonversi string ke dictionary
    try:
        word_index = ast.literal_eval('{' + tokenizer_content + '}')
    except Exception as e:
        print(f"Error parsing tokenizer content: {e}")
        return

    # Buat struktur tokenizer yang kompatibel dengan Keras
    tokenizer_json = {
        "class_name": "Tokenizer",
        "config": {
            "num_words": 50000,
            "filters": "!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n",
            "lower": True,
            "split": " ",
            "char_level": False,
            "oov_token": "<UNK>",
            "document_count": 0,
            "word_counts": {},
            "word_docs": {},
            "index_docs": {},
            "word_index": word_index
        }
    }

    # Simpan ke file JSON baru
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tokenizer_json, f, ensure_ascii=False, indent=2)

    print(f"Tokenizer berhasil dikonversi. Jumlah kata: {len(word_index)}")
    print("Contoh beberapa kata pertama:")
    for word, index in list(word_index.items())[:10]:
        print(f"{word}: {index}")


# Jalankan konversi
convert_tokenizer_json()