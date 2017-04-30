{
  "targets": [
    {
      "include_dirs" : [ ],
      "cflags_cc": [ '-Wall', '-pedantic', '-std=c++11', '-fexceptions' ],
      "libraries": [ '-L/usr/local/lib -lcrfsuite' ],
      "target_name": "crfsuite",
      "sources": [ 
         "src/main.cc", 
         "src/trainer_class.cc", 
         "src/tagger_class.cc"
      ]
    }
  ]
}
