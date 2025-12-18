use std::fs::File;
use std::io::{self, Write, BufWriter};

fn main() {
    menu_principal();
}

fn menu_principal() {
    loop {
        println!("  ________________________________________");
        println!(" / _____________________________________  \\");
        println!(" | |                                    | |");
        println!(" | | ________                .__        | |");
        println!(" | | \\______ \\ _____    _____|  |__     | |");
        println!(" | |  |    |  \\\\__  \\  /  ___/  |  \\    | |");
        println!(" | |  |    `   \\/ __ \\_\\___ \\|   Y  \\   | |");
        println!(" | | /_______  (____  /____  >___|  /   | |");
        println!(" | |         \\/     \\/     \\/     \\/    | |");
        println!(" | |                                    | |");
        println!(" | |____________________________________| |");
        println!(" \\________________________________________/\n");

        println!("\n 1. Lancer la création d'une Rainbow table");
        println!("___________________________________________");
        println!("\n 0. Quitter\n");
        
        print!("Votre choix : ");
        io::stdout().flush().unwrap();

        let mut choix = String::new();
        io::stdin().read_line(&mut choix).expect("Failed to read line");

        match choix.trim().parse::<u32>() {
            Ok(1) => creation_rainbow_table(),
            Ok(0) => {
                println!("Au revoir !");
                return;
            },
            _ => {
                println!("Choix invalide, veuillez réessayer.");
                continue;
            }
        }
    }
}

fn creation_rainbow_table() {
    let mut lowercase = false;
    let mut uppercase = false;
    let mut numbers = false;

    loop {
        println!("  ________________________________________");
        println!(" / _____________________________________  \\");
        // ... (ASCII art)
        println!(" \\________________________________________/\n");

        println!(" [{}] 1. Inclure les minuscules", if lowercase { "X" } else { " " });
        println!(" [{}] 2. Inclure les majuscules", if uppercase { "X" } else { " " });
        println!(" [{}] 3. Inclure les chiffres\n", if numbers { "X" } else { " " });

        println!(" 9. Étape suivante");
        println!("___________________________________________");
        println!("\n 0. Menu principal\n");

        print!("Votre choix : ");
        io::stdout().flush().unwrap();

        let mut choix = String::new();
        io::stdin().read_line(&mut choix).expect("Failed to read line");

        match choix.trim().parse::<u32>() {
            Ok(1) => lowercase = !lowercase,
            Ok(2) => uppercase = !uppercase,
            Ok(3) => numbers = !numbers,
            Ok(0) => return,
            Ok(9) => {
                if !lowercase && !uppercase && !numbers {
                    println!("\nERREUR : Vous devez choisir au moins une catégorie\n");
                    continue;
                }
                break; // Proceed to length selection
            },
            _ => println!("Choix invalide, veuillez réessayer."),
        }
    }

    // --- Character set and length selection ---
    let mut temp = Vec::new();
    if lowercase {
        temp.extend('a'..='z');
    }
    if uppercase {
        temp.extend('A'..='Z');
    }
    if numbers {
        temp.extend('0'..='9');
    }

    let nb_caracteres: usize;
    loop {
        print!("\nCombien voulez-vous de caractères ? ");
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        match input.trim().parse() {
            Ok(n) if n > 0 => {
                nb_caracteres = n;
                break;
            },
            _ => println!("Veuillez entrer un nombre entier positif."),
        }
    }

    println!("Création de la rainbow table en cours...");

    let file = File::create("rainbow_table.txt").expect("Impossible de créer le fichier.");
    let mut writer = BufWriter::new(file);

    generate(nb_caracteres, &temp, String::new(), &mut writer);
    
    writer.flush().unwrap();
    println!("\nRainbow table créée avec succès dans 'rainbow_table.txt'");
}

fn generate(k: usize, charset: &[char], prefix: String, writer: &mut BufWriter<File>) {
    if k == 0 {
        writeln!(writer, "{}", prefix).unwrap();
        return;
    }
    for &c in charset {
        let new_prefix = format!("{}{}", prefix, c);
        generate(k - 1, charset, new_prefix, writer);
    }
}
