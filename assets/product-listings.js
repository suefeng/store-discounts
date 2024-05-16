const getData = async () => {
  const url = "/scrapy_crawler/products.json";
  return await fetch(url).then((res) => res.json());
};

const createProduct = async () => {
  const root = document.getElementById("root");
  const storesData = await getData();
  storesData.map((store) => {
    const storeName = store.store_name;

    const heading = document.createElement("h1");
    heading.innerHTML = storeName;
    const section = document.createElement("section");
    section.setAttribute("id", storeName);
    section.appendChild(heading);

    const article = document.createElement("article");

    store.items.map((product) => {
      const h2 = document.createElement("h2");
      const a = document.createElement("a");
      const img = document.createElement("img");
      const p = document.createElement("p");

      h2.innerHTML = product.title;
      a.setAttribute("href", product.product_url);
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
      img.setAttribute("src", product.image_url);
      p.innerHTML = product.price;

      a.appendChild(h2);
      a.appendChild(img);
      a.appendChild(p);

      article.appendChild(a);
      section.appendChild(article);
    });

    root.appendChild(section);
  });
};

createProduct();