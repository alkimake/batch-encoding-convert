function encodeFiles($rootPath) 
{ 
    $directories = scandir($rootPath); 
    // Loop through each directory in the rootPath 
    foreach ($directories as $dir) 
    { 
        if (file_exists($fileName)) 
        { 
            // Read in the contents 
            $data = file_get_contents($fileName); 
            // Just display on the screen the file being modified 
            echo "Converting " . $fileName . "...\n"; 
            // Convert the contents 
            $data = iconv("UCS-2","UTF-8", $data); 
            // Write back out to the same file 
            file_put_contents($fileName,$data); 
        }  // end if file exists 
    }  // end loop for each directory in the root directory 
}  // end of function encodeFiles()  