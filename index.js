const trainer = require('./build/Release/crfsuite').TrainerClass;
const tagger = require('./build/Release/crfsuite').TaggerClass;

module.exports = { 
  Trainer: trainer,
  Tagger: tagger
}
