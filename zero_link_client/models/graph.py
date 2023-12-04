from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.edge import Edge
  from ..models.graph_ids import GraphIds
  from ..models.node import Node





T = TypeVar("T", bound="Graph")


@_attrs_define
class Graph:
    """ 
        Attributes:
            nodes (List['Node']):
            edges (List['Edge']):
            ids (Union[Unset, GraphIds]):
     """

    nodes: List['Node']
    edges: List['Edge']
    ids: Union[Unset, 'GraphIds'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()

            nodes.append(nodes_item)




        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()

            edges.append(edges_item)




        ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nodes": nodes,
            "edges": edges,
        })
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edge import Edge
        from ..models.graph_ids import GraphIds
        from ..models.node import Node
        d = src_dict.copy()
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in (_nodes):
            nodes_item = Node.from_dict(nodes_item_data)



            nodes.append(nodes_item)


        edges = []
        _edges = d.pop("edges")
        for edges_item_data in (_edges):
            edges_item = Edge.from_dict(edges_item_data)



            edges.append(edges_item)


        _ids = d.pop("ids", UNSET)
        ids: Union[Unset, GraphIds]
        if isinstance(_ids,  Unset):
            ids = UNSET
        else:
            ids = GraphIds.from_dict(_ids)




        graph = cls(
            nodes=nodes,
            edges=edges,
            ids=ids,
        )

        graph.additional_properties = d
        return graph

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
