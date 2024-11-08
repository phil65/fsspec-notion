__version__ = "0.0.1"

import fsspec

from fsspec_notion.notionfs import NotionFS


fsspec.register_implementation("notion", NotionFS)

__all__ = ["NotionFS"]
