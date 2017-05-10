{
  "targets": [
    {
      "include_dirs" : [ "src/liblbfgs-1.10/include", "src/crfsuite-0.12/include", "src/crfsuite-0.12/lib/cqdb/include"],
      "cflags_cc": [ '-O3', '-Wall', '-pedantic', '-std=c++11', '-fexceptions', '-DUSE_SSE', '-DUSE_SSE2' ],
      "target_name": "crfsuite",
      "sources": [ 
         "src/liblbfgs-1.10/lib/lbfgs.c",

         "src/crfsuite-0.12/lib/crf/src/crf1d_context.c",
         "src/crfsuite-0.12/lib/crf/src/crf1d_encode.c",
         "src/crfsuite-0.12/lib/crf/src/crf1d_feature.c",
         "src/crfsuite-0.12/lib/crf/src/crf1d_model.c",
         "src/crfsuite-0.12/lib/crf/src/crf1d_tag.c",
         "src/crfsuite-0.12/lib/crf/src/crfsuite.c",
         "src/crfsuite-0.12/lib/crf/src/crfsuite_train.c",
         "src/crfsuite-0.12/lib/crf/src/dataset.c",
         "src/crfsuite-0.12/lib/crf/src/dictionary.c",
         "src/crfsuite-0.12/lib/crf/src/holdout.c",
         "src/crfsuite-0.12/lib/crf/src/logging.c",
         "src/crfsuite-0.12/lib/crf/src/params.c",
         "src/crfsuite-0.12/lib/crf/src/quark.c",
         "src/crfsuite-0.12/lib/crf/src/rumavl.c",
         "src/crfsuite-0.12/lib/crf/src/train_arow.c",
         "src/crfsuite-0.12/lib/crf/src/train_averaged_perceptron.c",
         "src/crfsuite-0.12/lib/crf/src/train_l2sgd.c",
         "src/crfsuite-0.12/lib/crf/src/train_lbfgs.c",
         "src/crfsuite-0.12/lib/crf/src/train_passive_aggressive.c",

         "src/crfsuite-0.12/lib/cqdb/src/cqdb.c",
         "src/crfsuite-0.12/lib/cqdb/src/lookup3.c",
         "src/main.cc", 
         "src/trainer_class.cc", 
         "src/tagger_class.cc"
      ]
    }
  ]
}
