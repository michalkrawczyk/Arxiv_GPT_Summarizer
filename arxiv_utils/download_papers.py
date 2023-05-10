import arxiv
from tqdm import tqdm

import os
from typing import List


def download_paper_from_arxiv(id_list: List[str], output_dir: str = ".") -> List[str]:
    """ Download research papers from Arxiv by paper id

    Parameters
    ----------
    id_list: List[str]
        List with ids for each paper to download

    output_dir: str
        Directory where documents will be saved


    Returns
    -------
    papers_downloaded: List[str]
        List of paths for each downloaded file

    """
    papers_downloaded = []
    search = arxiv.Search(id_list=id_list)

    for paper in tqdm(search.results(), desc="Downloading files..."):
        file_path = paper.download_pdf(dirpath=output_dir)

        if os.path.isfile(file_path):
            papers_downloaded.append(file_path)

    return papers_downloaded


def download_recent_papers_by_querry(querry: str, limit: float = 10.0,
                                     output_dir: str = ".") -> List[str]:
    """ Download research papers from Arxiv by result of search querry

    Parameters
    ----------
    querry: str
        Search querry (e.g. 'Deep Learning')

    limit: float
        Maximum number of papers to download.

    output_dir: str
        Directory where documents will be saved

    Returns
    -------
    papers_downloaded: List[str]
        List of paths for each downloaded file

    """
    papers_downloaded = []
    search = arxiv.Search(
        query=querry,
        max_results=limit,
        sort_by=arxiv.SortCriterion.SubmittedDate)

    for paper in tqdm(search.results(), desc="Downloading files..."):
        file_path = paper.download_pdf(dirpath=output_dir)
        papers_downloaded.append(file_path)

    return papers_downloaded
