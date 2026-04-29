module.exports = function(text){
  const map = {
    AI: ["ai","neural","intelligence"],
    ML: ["learning","model"],
    Security: ["security","attack","encryption"],
    Data: ["data","analysis","dataset"]
  };

  text = text.toLowerCase();
  let tags = [];

  for(let key in map){
    map[key].forEach(w=>{
      if(text.includes(w)) tags.push(key);
    });
  }

  return [...new Set(tags)];
};